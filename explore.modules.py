import random

# See what's in the module
print("Functions in random module:")
print([name for name in dir(random) if not name.startswith('_')])
print()

# Get help on specific function
print("Help for randint:")
print(help(random.randint))

## Online Documentation

## The best resource: **Python's Official Documentation**

### For Standard Library Modules
# Visit: **https://docs.python.org/3/library/**


# This has EVERY built-in module with examples!

# **Example: Want to learn about random?**
# 1. Go to https://docs.python.org/3/library/random.html
# 2. Read the overview
# 3. Scroll through function list
# 4. See examples

### How to Read Documentation

# When you see this in documentation:

random.randint(a, b)