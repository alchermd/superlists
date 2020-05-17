# Python TDD

A Django app built with TDD

## Notes

- Don't test constants.
	- Instead of testing HTML responses, write a test that checks if the correct template is rendered.
- The TDD Process:

![](https://www.obeythetestinggoat.com/book/images/twp2_0403.png)

- Furthermore, the TDD Process with Unit and Functional tests:

![](https://www.obeythetestinggoat.com/book/images/twp2_0404.png)

### Red/Green/Refactor and Triangulation
The unit-test/code cycle is sometimes taught as Red, Green, Refactor:

- Start by writing a unit test which fails (Red).

- Write the simplest possible code to get it to pass (Green), even if that means cheating.

- Refactor to get to better code that makes more sense.

So what do we do during the Refactor stage? What justifies moving from an implementation where we "cheat" to one we’re happy with?

One methodology is eliminate duplication: if your test uses a magic constant, and your application code also uses it, that counts as duplication, so it justifies refactoring. Removing the magic constant from the application code usually means you have to stop cheating.

I find that leaves things a little too vague, so I usually like to use a second technique, which is called triangulation: if your tests let you get away with writing "cheating" code that you’re not happy withwrite another test that forces you to write some better code.

### Concepts

- Regression

	When new code breaks some aspect of the application which used to work.

- Unexpected failure

	When a test fails in a way we weren’t expecting. This either means that we’ve made a mistake in our tests, or that the tests have helped us find a regression, and we need to fix something in our code.

- Red/Green/Refactor

	Another way of describing the TDD process. Write a test and see it fail (Red), write some code to get it to pass (Green), then Refactor to improve the implementation.

- Triangulation

	Adding a test case with a new specific example for some existing code, to justify generalising the implementation (which may be a "cheat" until that point).

- Three strikes and refactor

	A rule of thumb for when to remove duplication from code. When two pieces of code look very similar, it often pays to wait until you see a third use case, so that you’re more sure about what part of the code really is the common, re-usable part to refactor out.

- The scratchpad to-do list

	A place to write down things that occur to us as we’re coding, so that we can finish up what we’re doing and come back to them later.

### Testing "Best Practices" 

- Ensuring test isolation and managing global state

	Different tests shouldn’t affect one another. This means we need to reset any permanent state at the end of each test. Django’s test runner helps us do this by creating a test database, which it wipes clean in between each test. 

- Avoid "voodoo" sleeps
	
	Whenever we need to wait for something to load, it’s always tempting to throw in a quick-and-dirty time.sleep. But the problem is that the length of time we wait is always a bit of a shot in the dark, either too short and vulnerable to spurious failures, or too long and it’ll slow down our test runs. Prefer a retry loop that polls our app and moves on as soon as possible.

- Don’t rely on Selenium’s implicit waits
	
	Selenium does theoretically do some "implicit" waits, but the implementation varies between browsers, and at the time of writing was highly unreliable in the Selenium 3 Firefox driver. "Explicit is better than implict", as the Zen of Python says, so prefer explicit waits.