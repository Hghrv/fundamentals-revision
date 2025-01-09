# Recursion

### ghost_buster

In `recursion.py`, there is a _perfectly_ good function that iterates through a list of dictionaries, in order to hunt down ghostly apparitions that are haunting the list.

You'll find our test suite in `test_recursion.py`. Every test is currently being skipped by our handy pytest decorator. You should make sure they all pass one by one.

What's this? One of them doesn't pass?

Iteration is wonderful, when we _know_ what data looks like. But when we don't, we have to check a lot of conditions, which becomes unwieldy.

1. Use recursion in in `ghost_buster` to pass all the tests.

2. There's an extra test that we haven't written - it's to do with the data we've passed in! What should we do to make sure it's ok? 
`Student's answer: we should ensure integrity of data trhough a purity test` 