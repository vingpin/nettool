# Vingpin Network tool
Simple Python script to execute some basic network functions on a container. 

## Build and run

```
git clone https://github.com/vingpin/nettool.git

cd nettool

docker build . -t vingpin/nettool

docker run -d -p 8122:8122 vingpin/nettool
```

## Examples
Select the action

![tool](https://github.com/vingpin/nettool/blob/3809be551f7c79fcff4ffb82d0416a1515a36c9b/image/nettool.png)

Traceroute example

![Trace](https://github.com/vingpin/nettool/blob/3809be551f7c79fcff4ffb82d0416a1515a36c9b/image/trace.png)


## License
  Copyright (c) 2023 Lars Gustavsson <lars@vingpin.se>

  Permission is hereby granted, free of charge, to any person obtaining a copy
  of this software and associated documentation files (the "Software"), to
  deal in the Software without restriction, including without limitation the
  rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
  sell copies of the Software, and to permit persons to whom the Software is
  furnished to do so, subject to the following conditions:

  The above copyright notice and this permission notice shall be included in
  all copies or substantial portions of the Software.

  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
  FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE
  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
  FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
  IN THE SOFTWARE.
