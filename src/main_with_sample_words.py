import csv
import functools
import heapq
import random

from pyspark import SparkContext, SparkConf
from aylienapiclient import textapi

class Exercise:

    @staticmethod
    def extractKeywords(url):
        random_list_of_words = url.split(",")
        return {w: 1 for w in random_list_of_words}

    @staticmethod
    def reduceKeywords(a, b):
        for k in b.keys():
            if not a.has_key(k):
                a[k] = b[k]
            else:
                a[k] += b[k]
        return a

    # Outputs the top 20 keywords in the urls
    @staticmethod
    def outputStats(hist):
        t = {}
        for k in hist:
            if t.has_key(hist[k]):
                t[hist[k]].append(k)
            else:
                t[hist[k]] = [k]

        values = t.keys()
        sorted(values)

        out = []
        for i in xrange(20):
            if len(values) == 0:
                break

            highestValue = values[-1]
            out.append(t[highestValue].pop())
            if len(t[highestValue]) == 0:
                values.pop()

        return out


def main():
    NUMBER_OF_PARTITIONS = 5
    client = textapi.Client("82786a30", "10973cc5ea2d4b57d83daa9d094c2693")

    # create Spark context with Spark configuration
    conf = SparkConf().setAppName("Read Text to RDD - Python")
    sc = SparkContext(conf=conf)

    # read input text file to RDD
    urls = sc.textFile('res/urls.csv', NUMBER_OF_PARTITIONS)

    keywords = urls.map(Exercise.extractKeywords)

    totalExercise = keywords.reduce(Exercise.reduceKeywords)

    with open('res/topTwenty.csv', 'wb') as f:
        topTwenty = Exercise.outputStats(totalExercise)
        w = csv.writer(f)
        for i in topTwenty:
            w.writerow([i])


if __name__ == "__main__":
    main()

