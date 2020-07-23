FlapPyBird-Env
===============

FlapPyBird game wrapped as gym environment. Base code forked from https://github.com/sourabhv/FlapPyBird.

<img src="rec.gif" width="450" height="700" alt="Game recording"/>

Usage
===============
Install the package:
```bash
$ python setup.py install
```

In your code import the package and create gym environment:

```python
from FlapPyBird_Env.flappy_env import FlappyEnv

env = FlappyEnv()
```