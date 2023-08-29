# Copyright (c) 2023 Lars Gustavsson <lars@vingpin.se>

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

from fastapi import FastAPI,  Request
from fastapi.responses import HTMLResponse
from fastapi import Form
from fastapi.templating import Jinja2Templates
import subprocess
templates = Jinja2Templates(directory="templates")
app = FastAPI()


def format(unformated):
    formatted_output = unformated.replace('\\n', '\n')
    formatted_output = formatted_output.replace('b\'', '')
    formatted_output = formatted_output[:-1]
    formatted_output = formatted_output.strip()
    return formatted_output


def ping(host):
    host = host.strip()
    command = ["ping", "-c", "2", "-w", "1", host]
    s = subprocess.run(command, capture_output=True)
    print(s.stderr)
    s = str(s.stdout)
    return format(s)


def trace(host):
    host = host.strip()
    command = ["traceroute", "-n", "-w", "1", host]
    s = subprocess.run(command, capture_output=True)
    print(s.stderr)
    s = str(s.stdout)
    return format(s)


def route():
    command = ["ip", "route"]
    s = subprocess.run(command, capture_output=True)
    print(s.stderr)
    s = str(s.stdout)
    return format(s)


def ip():
    command = ["ip", "addr"]
    s = subprocess.run(command, capture_output=True)
    print(s.stderr)
    s = str(s.stdout)
    return format(s)


def arp():
    command = ["arp", "-n"]
    s = subprocess.run(command, capture_output=True)
    print(s.stderr)
    s = str(s.stdout)
    return format(s)


@app.post("/submit/")
async def submit(request: Request, nm: str = Form(None),
                 action: str = Form(...)):
    match action:
        case "ping":
            if (not nm):
                return templates.TemplateResponse("start.html",
                                                  {"request": request,
                                                   "output":
                                                   "Did you forget the IP/Hostname?"
                                                   })
            return templates.TemplateResponse("start.html",
                                              {"request": request,
                                               "output": ping(nm),
                                               "nm": nm})
        case "trace":
            if (not nm):
                return templates.TemplateResponse("start.html",
                                                  {"request": request,
                                                   "output":
                                                   "Did you forget the IP/Hostname?",
                                                   "nm": ""
                                                   })
            return templates.TemplateResponse("start.html",
                                              {"request": request,
                                               "output": trace(nm),
                                               "nm": nm})
        case "route":
            if (not nm):
                return templates.TemplateResponse("start.html",
                                                  {"request": request,
                                                   "output": route(),
                                                   "nm": ""})
            return templates.TemplateResponse("start.html",
                                              {"request": request,
                                               "output": route(),
                                               "nm": nm})
        case "arp":
            if (not nm):
                return templates.TemplateResponse("start.html",
                                                  {"request": request,
                                                   "output": arp(),
                                                   "nm": ""})
            return templates.TemplateResponse("start.html",
                                              {"request": request,
                                               "output": arp(),
                                               "nm": nm})
        case "ip":
            if (not nm):
                return templates.TemplateResponse("start.html",
                                                  {"request": request,
                                                   "output": ip(),
                                                   "nm": ""})
            return templates.TemplateResponse("start.html",
                                              {"request": request,
                                               "output": ip(),
                                               "nm": nm})
        case _:
            return templates.TemplateResponse("start.html",
                                              {"request": request,
                                               "output": "Now you broke it!",
                                               "nm": nm})


@app.get("/", response_class=HTMLResponse)
async def start(request: Request):
    output = ""
    return templates.TemplateResponse("start.html", {"request": request,
                                                     "output": output})


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8122)
