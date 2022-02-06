#!/usr/bin/python
import os
import re
import sys

def SubjectHelper(subject):
    return subject

def GetBySubject(subject, search_range, flag):
    subject = subject.strip("\n")
    subject_re = SubjectHelper(subject).replace("\"", "\\\"").replace("\`", "\\\`")

    cmd = "git log --pretty=oneline " + search_range + " | grep -F \"" + subject_re + "\""
    git_log = os.popen(cmd).readlines()
    for log in git_log:
        log = log.strip("\n")
        __commit = log[:40]
        __subject = log[41:]
        if SubjectHelper(subject) == SubjectHelper(__subject):
            __version = ""
            if flag == True:
                __version = os.popen("git name-rev " + __commit).readline().strip("\n")[41:]
            return __commit, __subject, __version
    return None, None, None

def GetByCommit(commit, search_range, flag):
    subject = os.popen("git log --pretty=oneline -n 1 " + commit).readline()[41:]
    return GetBySubject(subject, search_range, flag)
 
def main():
    commit = sys.argv[1]
    search_range = "v5.10..stable/linux-5.10.y"
    commit, subject, version = Get(subject, search_range, flag)
    print(commit, subject, version)

if __name__ == '__main__':
    main()



