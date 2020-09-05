# Contributing

---

**If you found a security vulnerability, do NOT open an issue. Please, email
mjnramos@protonmail.com instead. Thank you!** If you are unsure if you detected
a security vulnerability, prefer the email approach.

---

Thank you for considering contributing to this project. This project was
developed to accept the contribution of talented people, like you!

In this document, you find the guidelines for contributing to this application.
While following these guidelines, you show respect the time of the developers
managing and developing this open source project. In return, they will
reciprocate that respect in addressing your issue, assessing changes, and
helping you finalize your contribution.

You may contribute to this project in several ways, depending your own
interests. You may spread the word to others, write tutorials, improve our
documentation, submit bug reports, present feature requests and/or writing
code to be incorporated here.

Before submitting a bug or a feature request, please confirm that your issue is
not being already in a discussion started by a third party.


## Expectation and responsibility

* Ensure that your contribution does not affects cross-platform compatibility.
* Open an issue before contributing. Be transparent on discussion and accept
feedback.
* Be respectful to all members, even when you disagree with them. All
contributions should be constructive.
* Focus on the best interest of the project.
* Ensure consistency with the previous existing materials.
* Review your changes carefully and confirm that you known all the meaning of
the materials you provide.
* Do not rush it! Take all the time you need, so that you present a final
fantastic work.
* Avoid non open source sources at all cost!
* Test your materials before submitting them.
* Be open minded to new members, with different background. Diversity is good.
* On opening an issue, use the appropriate labelling. More on labels in the end
of this document.
* Understand and follow the commit template that is available in the end of
this document. We may reject commits messages that are confusing or misleading.


## Getting started

If you are looking for your first contribution, please be welcomed. Everyone
had a first time!

Please follow this guide to contribute:

1. Open an issue with the indication of the changes you want to make, so that
it may be discussed before work done;
2. Fork this repository;
3. Apply all changes on your forked repository;
4. When you are happy with our changes, prepare the pull request submission by
reading again the `Expectation and responsibility` and `Check list` segments;
5. Open a detailed pull request.


## Check list

Before opening a pull request, please ensure you comply with this check list.

* [ ] Confirm that spelling and grammar is ok;
* [ ] Clean up unnecessary comments;
* [ ] Test your materials (again and again!);
* [ ] Confirm if documentation needs to be updated, including `README.md` file
or any metadata as `.gitignore`, etc. Say that in your pull request.
* [ ] Ensure that you are complying with PEP8 formatting, by running
`pycodestyle` on your modified files.
* [ ] Please check **How to ... submit code** (below) for additional
considerations.


## How to...

### ... report a bug

**If you found a security vulnerability, do NOT open an issue. Please, email
mjnramos@protonmail.com instead. Thank you!** If you are unsure if you detected
a security vulnerability, prefer the email approach.

Before submitting a bug, test it (again!):

* [ ] Can you reproduce the bug?
* [ ] Can you reproduce the bug after cleaning cookies, cache, configuration
files, etc?
* [ ] Can you reproduce the bug in private mode?
* [ ] Can you reproduce the bug in a different machine?
* [ ] Can you reproduce the bug in a different connection?
* [ ] Is this the first time the bug is detected? If not, do not issue a new
issue. Instead, contribute to the issue already opened.

When filling and issue, make sure you use this template:
~~~
# Bug report


## Tests

(Remove this line. Change `Not tried` to `Yes` or `No`, when tested. You may
use `Not sure` or `Not always`, but explain those answers in description.)

* Can you reproduce the bug? [Not tried]
* Can you reproduce the bug after cleaning cookies and cache? [Not tried]
* Can you reproduce the bug in private mode? [Not tried]
* Can you reproduce the bug in a different machine? [Not tried]
* Can you reproduce the bug in a different connection? [Not tried]


## Description

(Change this line with a complete, clear and explicit description of the bug
you are reporting.)


## Behaviour

(Change this line with a behaviour notice. Reply to 2 questions: What should be
expected behaviour? What is the real behaviour?)


## Steps to reproduce

(Change this line with the step-by-step guide requited to reproduce the bug.)


## Version

(Change this line with indication of the version you are using. Is that an
stable version or a development one?)


## Environment

(change this line with a description of the environment of your installation,
if possible. Indicate operating system, version, architecture, etc.)


## Additional comments

(Change this line with any additional comment you would like to make.)

~~~

Please, do not use a bug reporter to ask questions!


### ... suggest a feature

Keep in mind which is this project mission (refer to [README](README.md)).

Please, consider your feature carefully. You are probably not alone and your
feature will help others. Anyway, this may be the first that that the
maintainers front this idea, so you need to make it clear.

* [ ] Why is this feature relevant?
* [ ] Who will benefit with this feature?

Present you feature request as an issue, using this template:
~~~
# Feature request


## Description

(Change this line with a complete, clear and explicit description of the
feature you are requesting.)


## Behaviour

(Change this line with a behaviour notice. Reply to 2 questions: What should be
expected behaviour? What is the real behaviour?)


## Advantages

(Change this line with the advantages of implementing this feature.)


## Disadvantages

(Change this line with possible disadvantages that may appear if your feature
becomes accepted.)


## Additional comments

(Change this line with any additional comment you would like to make.)

~~~


### ... submit code

Main notes:

* Please, keep yourself a time to learn about clean code!
* Your code should be [PEP 8](https://pep8.org/) compliant. Before sending a
pull request, test your code with `pycodestyle`, to make sure of this guideline;
* Use double quotes on strings;
* Keep your functions simple: A function should only have one function.
* Write code, variables and comments in english.
* Always indicate the issue you are solving for.
* If you fix any bug, create a test to grantee that the bug is solved. Your
test should catch the bug if it comes back.

Please note, that the process of reviewing and accepting your code requires
time. Also, your code is not static and will need changes in the future. By not
following the standard stiles described, your code may be refused.

Remember: This is an open source project. Keep in mind that your code does not
violate our license and that you have followed the legal requirements while
coding to this project.

Before accepting a pull request, your code will be reviewed by the maintainers.
Pull requested will be evaluated as soon as possible.


## Issue labels

* `Bug`: To report general bugs;
* `Documentation`: Improvements or additions to documentation;
* `Duplicate`:  This issue or pull request already exists. Do not start issues
with this label;
* `Feature`: To request a new feature or change of any kind;
* `Invalid`: Issue does not seems right. Do not start issues with this label;
* `Question`: To ask general questions that do not overlap in the previous
labels;
* `Wontfix`: This will not be worked on. Do not start issues with this label;
* `Other`: If it does not fit in any other label, it will fit here!


## Git commit template

If you follow this git commit template, your code is in the good track to be
accepted. This template was designed to be fast on using and simple on reading.

A commit should do one think only!

Each commit message consists of a header, a body and a footer. The header has a
special format that includes a type, an application and a subject. Do not use
capital letters unless required (e.g. acronyms, names, etc).

~~~
[<type>] <subject>

<body>

<issue fix>
<pep8 note>
~~~

To be in line with pep8, each line of the commit message should be 79
characters long on maximum, **except for the first line whose maximum should be
72 characters**!


**Types:**

* `feature`: A new feature is being included.
* `bugfix`: A bug is being fixed.
* `doc`: The change only applies to documentation.
* `ftest`: New tests are being featured to the program.
* `minor`: Small change that should not affect code (e.g. pep8 formatting).
* `unknown`: An unknown type that should be described in body. Probably your
code will be rejected if you use this type.


**Subject:** A very short (and clear) indication of the change committed. Use
imperative present tense (e.g. `change` instead of `changed`/`to change`). Do
not end with a dot (`.`). This whole line should be at maximum 72 characters
long.

**Body**: Multiple lines may be used. Follow the same rules as subject, but
permits motivation for the change and/or contrast this with previous behaviour.
Please use a descriptive approach instead of a bullets one. Maximum line size
is 79 characters.

**Issue fix**: Indicate the issue you are resolving (e.g. `fix #<issue>`). You
may (but probably you should not) resolve multiple issues at the same time
(e.g. `fix #<issue1> #<issue2>`). You also may (but definitely should not) use
the statement `no issue fix`.

**PEP8 note**: Please confirm that you ran `pycodestyle` on your files, and
that all of your files are under the PEP8 norms. Use `pep8 pass` for valid PEP8
formatting. You may also (but should not) use `pep8 not tested`, `pep8 fail` or
`pep8 not applicable` (to be used on documentation).

For examples, please refer to commits already approved.
