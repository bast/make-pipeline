[![License](https://img.shields.io/badge/license-%20MPL--v2.0-blue.svg)](../master/LICENSE)


# Data processing pipeline example

This can be used to motivate and teach Makefiles.


## Examples

Process one file:

```shell
$ cat data/lorem.in | ./count.py | ./plot.py
```

Process all files:

```shell
$ make [-jN]
```


## Makefile

```makefile
SRCS = $(wildcard data/*.in)

OBJS = $(patsubst %.in,%.tmp,$(SRCS))
OBJS += $(patsubst %.in,%.out,$(SRCS))

all: $(OBJS)

# otherwise intermediate tmp files would be deleted
.PRECIOUS: %.tmp

%.tmp: %.in
	cat $< | ./count.py > $@

%.out: %.tmp
	cat $< | ./plot.py > $@
```
