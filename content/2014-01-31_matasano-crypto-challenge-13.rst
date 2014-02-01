Matasano Crypto Challenges, Exercise 13
=======================================

:date: 2014-01-31 18:30
:tags: crypto
:slug: matasano-crypto-challenge-13
:author: ninly

I started up this blog as a place to muse on current tech projects and
share what I'm doing and learning. Then I went and got re-mired in my
Matasano code, which I can't share.

Last spring, on a tip from Steve_, I spent a bunch of time working on the then-brand-new
`Matasano Crypto Challenges`_, which you should go read about if you're
not already familiar.

.. _Steve: http://illruminations.com/

.. _`Matasano Crypto Challenges`: http://www.matasano.com/articles/crypto-challenges/ 

It was perfect for me in a lot of ways. In addition to my longstanding
interest in things cryptological, it was a perfect venue to try my hand
at more "practical" code, as I described in a `previous post`_. The
exercises are (more or less) graded, and in many cases tell you roughly
how you're going to approach the goal. I plugged at the first set of
exercises for a few days, and felt like I'd wrapped my head around
something new. I finished the first set and received the second, and
things got even more interesting.

.. _`previous post`: http://ninly.github.io/posts/2014/01/pip-and-virtualenv-sans-magic/

Without revealing any content, I'll say that exercise 12 was
particularly fun, engaging, and rewarding to accomplish. I felt quite a
bit of momentum, and ready to tackle whatever came at me.

Then, I hit exercise 13. I got stuck.

I think the exercise assumed a certain level of practical familiarity
with web-transaction infrastructure. [*]_ User authentication, cookies,
that sort of thing. I know more or less how that stuff works, but have
little hands-on experience actually implementing them for a production
website. Building on what I'd learned from the exercises thus far, I
quickly sort of painted myself into a corner, feeling like every avenue
I pursued wound up a dead end.

Having a brand-new baby in the house also didn't help. Time devoted to
the project evaporated for a time.

There was a HDD failure on my dev/hacking machine, too, but that's
another post.

This week, after several months away from the code, I revisited the
Matasano Crypto Challenges. I worked through my existing code, reminding
myself what I'd done and how. I reimplemented a few functions, just to
see if different ways to do things seemed cleaner or appealed more.
Some did. And, as a lot of coders say, reading your own code months or
years later can be painful, but also eye-opening.

Then I approached that sticky wicket, exercise 13, with a fresh mind. I
didn't even look at the code I'd written for it; I just reread the
assignment, and started coding.

I got my test code to pass yesterday. Turns out, it wasn't that bad.  My
solution isn't perfect: I'm not entirely happy with some of the
assumptions it makes (again, I'm trying not to reveal anything about the
exercise content here), but it works, and at least I have something to
improve on now.

And, best of all, now I get to think about exercise 14.

.. [*] See `this Pinboard blog post`_ for a good description of the Matasano Crypto Challenges by someone who *does* have that familiarity.

.. _`this Pinboard blog post`: https://blog.pinboard.in/2013/04/the_matasano_crypto_challenges/
