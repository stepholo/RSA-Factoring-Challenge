RSA FACTORING CHALLENGE
=======================
Requirement - General
---------------------

You can choose the language of your choice.
OS needs to be Standard Ubuntu 20.04 LTS/

Factors
=======

This program factorizes natural numbers into a product of two smaller numbers. It takes as input a file containing natural numbers to factor, with one number per line. The program assumes that all lines in the file will be valid natural numbers greater than 1, and there will be no empty lines or spaces before or after the valid number. The file will always end with a new line.

Usage
-----

To use the program, follow these steps:

1.  Download the repository and navigate to the program's directory.
    
2.  Run the program using the following command:
    
The usage for factoring challenge 
---------------------------------
bash

```bash
./factors <file>
```

The usage for RSA challenge
---------------------------
bash

```bash
./rsa <file>
```

Replace `<file>` with the path to the file containing the numbers to factor.

3.  The program will output the factorization results in the format `n=p*q`, where `n` is the input number and `p` and `q` are the factors.

Output Format
-------------

The program provides one factorization per line. The factors `p` and `q` in the output don't have to be prime numbers. Here's an example of the output format:

markdown

```markdown
24=4*6
35=5*7
```

Dependencies and Execution Environment
--------------------------------------

The program is designed to run without any dependencies. You do not need to install any additional software or libraries. It should work on most Unix-like systems.

Time Limit
----------

To ensure efficiency, the program has a time limit of 5 seconds. If it hasn't finished within this time, it will be automatically terminated.

Challenge
---------

RSA Laboratories states that for each RSA number `n`, there exist prime numbers `p` and `q` such that `n = p × q`. The challenge is to find these two primes, given only `n`.

This task is similar to Task 0, with the following differences:

*   `p` and `q` are always prime numbers.
*   There is only one number in the input file.

Images
------

Below are the images related to the challenge:
![Factoring Challenge](factoring_challenge.png)
![RSA Challenge](RSA_TEST.png)


Good luck, and let's see how far you can go in less than 5 seconds!

---