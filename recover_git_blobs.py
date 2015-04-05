# Code modified from original StackOverflow answer provided by 'Boy' - http://stackoverflow.com/a/20997627


# 1) Run: git fsck --cache --unreachable $(git for-each-ref --format="%(objectname)") > allhashes.txt
# 2) Run: python recover_git_blobs.py allhashes.txt

import argparse
from subprocess import call


def main():
  
  parser = argparse.ArgumentParser()
  parser.add_argument("git_dangling_hashes_filename", help="the file containing the exported git hashes".)
  
  args = parser.parse_args()
  
  output_filename = "./recovered_file_{0}.txt"
  
  i = 1

  git_dangling_hashes = read_file(args.git_dangling_hashes_filename)
  
  # For each hash exported to file by git, call 'git show' and write the contents of the file to a new .txt file.
  for git_hash in git_dangling_hashes:
      f = open(output_filename.format(str(i)), "wb")
      call(["git", "show", git_hash],stdout=f)
      i+=1

def read_file(file_path):

    try:

        commits = []

        with open(file_path, 'r') as open_file:

            for i, line in enumerate(open_file):

                commits.append(line.strip())

    except IOError as e:

        if e.errno == errno.ENOENT:
            raise IOError("File not found: {0}".format(file_path))

        print "Error: Unable to read data - {0}".format(file_path)

    return commits

if __name__ == '__main__':
    main()
