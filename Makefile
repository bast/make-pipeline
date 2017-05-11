SRCS = $(wildcard data/*.in)
OBJS = $(patsubst %.in,%.out,$(SRCS))

all: $(OBJS)

# otherwise intermediate tmp files would be deleted
.PRECIOUS: %.tmp

%.tmp: %.in
	cat $< | ./count.py > $@

%.out: %.tmp
	cat $< | ./plot.py > $@
