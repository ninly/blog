LabVIEW Break!
==============

:date: 2014-07-01 07:10
:tags: linux-kernel, labview
:slug: labview-break
:author: ninly

As of a month or so ago I was still going strong with the Eudyptula
Challenge tasks: building development kernels, hacking on dynamically
loadable modules, exploring intricacies of git, and generally learning
my way around the internal structures that make Linux tick.

I had just begun to really dig into the whole idea of concurrency and
the mechanisms (locking and so forth) and race condition caveats the
kernel and its documentation have to offer. Then something came up.

Cutscene with BBQ
-----------------

Our local National Instruments LabVIEW User Group runs a pretty tight
ship. I haven't used LabVIEW itself much (I have messed around with
it quite a bit), but the test equipment I've been working with for
the past couple of years runs on LabWindows/CVI -- NI's C environment
("C with training wheels", a coworker of mine likes to say). So I'm
not especially proficient in LabVIEW, but I do attend the user group
meetings: There's usually a fairly interesting demonstration of its
features or of some real-world deployment. The whole concept of dataflow
programming is interesting to me for a few reasons, too, related in part
to my longtime interest in audio processing -- cf. Pure Data, Max, even
(going back a few extra years) Turbosynth.

And I'd be lying if I told you the free barbecue they brought into the
meetings wasn't a factor.

Last year the user group offered its regular attendees the chance to
take NI's CLAD certification exam at no cost. It took a little bit of
study, but the CLAD is their entry-level certification. The exam is
fairly basic, and I passed without much difficulty.

If you're not familiar with LabVIEW, it's pretty neat stuff. It's
a full-featured high-level language, but the development interface
is based on the concept of *dataflow*. That is, instead of writing
text-based code, you connect functional blocks together with graphical
"wires". It is used extensively in a number of industries, particularly
in testing and industrial data-aquisition applications. If you're just a
curious amateur the software isn't cheap, but if (like me) you work in
an environment where it is available, it's worth checking out.

Would You Like an Exam with That?
---------------------------------

This spring they offered a similar opportunity, but for people who
aready have the CLAD certification they offered the CLD exam -- their
full professional development certification.

Great, I thought -- not a chance I should pass up. It normally costs
about $400. *But*... the CLD is a far more challenging exam. It's geared
not only to proficiency, but to *facility* with the software and its
graphical language.

It's a 4-hour practical exam. They shut you in a room, give you
a sealed spec for an application of nontrivial complexity (typical
textbook state machines -- modelling behavior of systems like ATMs,
vending machines, and so forth -- but with a lot of real-world-like
functions, constraints, and corner cases). Without any external
references or breaks, you have to build a working application.

Four hours may seem like a long time, but it's widely regarded as the
most challenging aspect of the CLD exam. To implement the typically
specified complexity in the time allotted, you really have to know
your way around the software *and* be able to make quick decisions about
how to implement the application's logic.

There's not any wiggle room. You can't take breaks or use your phone. No
Internet or reference manual is available (other than LabVIEW's built-in
help). When time runs out, you save your code to a thumb drive, seal it
in an envelope, and wait several weeks for an anonymous NI engineer to
review your code. To fast-forward a bit: I took the exam back in May, and
still haven't received my results.

Cram Time
---------

As I mentioned, I haven't really used LabVIEW that much. When I heard that I
could take the CLD exam for free, and that I only had a few weeks to prepare...
I did a quick deep-dive into some LabVIEW books, familiarizing myself with some
of the conventions and best practices for more intricate applications (things
like event-driven logic, queued state machines, and producer-consumer
frameworks, among others).

I learned a ton, but I would be shocked if I passed. That is really OK
-- getting the certification would have been lovely, but the experience
of preparing for and taking the exam were my primary goals. I got a
whole lot out of it, not only in that little bout of self-training, but the
exam itself was pretty eye-opening, too. Not only will I be far better
prepared to approach the exam next time it is offered, but it has given
me some ideas for things I could do with LabVIEW in the meantime.

Back to the Penguin
-------------------

Of course, through all of that, my kernel-coding efforts were on hold.
Since the CLD exam, I've spent the last few weeks refamiliarizing myself
with the Eudyptula Challenge task I was on when I set it down. It took
less time than I feared to find my bearings; I had been in the middle of
Task 8, and submitted it just the other day. From what I understand, it
takes about a week for Little to respond to that one (one of the more
complex tasks), so I'm using the downtime to run through kernel-build
processes again, as that's a skill that tends to languish when I don't
use it regularly, and it's been a while. I have a feeling I'll be using
it again soon.
