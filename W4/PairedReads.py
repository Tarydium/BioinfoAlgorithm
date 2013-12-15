'''
    Solve the String Reconstruction from Read-Pairs Problem.
    Input: An integer d followed by a collection of paired k-mers PairedReads.
    Output: A string Text with (k, d)-mer composition equal to PairedReads.
'''

from EulerianPath import EulerianPath, JoinPathtoString
from DeBruijn import DeBruijnKmer

class PReads:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __eq__(self, other):
        return other and self.left == other.left and self.right == other.right

    def __hash__(self):
        return hash((self.left, self.right))


def PReadsParser(seqs):
    pass

def PairedReads(seqs, d):
    # node_dict is mapping from number to PReads class
    graph, node_dict = PReadsParser(seqs)
    #EulerianPath
    pass

def EulerianString(seqs):
    graph = DeBruijnKmer(seqs)
    path  = EulerianPath(graph)
    return JoinPathtoString(path)

def PairedCheating(seqs_start, seqs_end, d):
    # This is a cheating way to find the right sequence
    print EulerianString(seqs_start)
    print EulerianString(seqs_end)

def PairfileParser(infile):
    flag = 1
    startseqs = []
    endseqs = []
    for line in open(infile):
        content = line.strip()
        if flag:
            d = int(content)
            flag = 0
            continue
        start, end = content.split("|")
        startseqs.append(start)
        endseqs.append(end)
    return d, startseqs, endseqs

def TestClass():
    first = PReads("A","C")
    second = PReads("D","C")
    third = PReads("A","C")
    print hash(first)
    print hash(second)
    print hash(third)
    d, start, end = PairfileParser("tmp")
    PairedCheating(start, end, d)

if __name__ == "__main__":
    TestClass()
