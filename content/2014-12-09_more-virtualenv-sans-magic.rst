More virtualenv (sans) magic
============================

:date: 2014-12-09 12:00
:tags: python, dependencies
:slug: more-virtualenv-sans-magic
:author: ninly

Several months back I was figuring out how to use pip and virtualenv,
and generally having a pretty good time with my python development
experience. However, I kept running into interesting code examples and
projects that required matplotlib and the numpy/scipy stack. Since I've
also been trying to get familiar with mathematical modeling, analysis
and visualization techniques, these are indispensable dependencies.

I could (and had) play with them "raw", but ran into problems when I
tried to enjoy the control and isolation afforded by virtualenv. Last
week, though, in one of my periodic attempts to comb through dependency
installations, I stumbled on `this gist`_, and it cleared up all my
problems. I haven't delved into whatever reasons may have existed for my
previous difficulties, but if you're having trouble, maybe it will help
you. All I did was to set up a new virtual env and pip-install my way
through the list. It... just worked, for the most part (thanks,
fyears_!), although I did have to update some fortran-compiler stuff
that numpy needed.

.. _this gist: https://gist.github.com/fyears/7601881

.. _fyears: https://www.fyears.org/
