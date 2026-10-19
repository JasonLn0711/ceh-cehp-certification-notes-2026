"""One progress adapter; JSON stdout belongs exclusively to command results."""
import json,os,re,sys,time

def sanitize(text):
    text=re.sub(r'(?i)(authorization\s*[:=]\s*)(?:bearer\s+)?[^\s,;]+',r'\1[REDACTED]',text)
    text=re.sub(r'(?i)((?:api[_-]?key|password|access[_-]?token|secret)\s*[:=]\s*)[^\s,;]+',r'\1[REDACTED]',text)
    return re.sub(r'(https?://)[^/@\s]+:[^/@\s]+@',r'\1[REDACTED]@',text)

class Progress:
    def __init__(self,plain=False):
        self.tty=sys.stderr.isatty() and not plain and os.environ.get('TERM')!='dumb';self.start=time.monotonic();self.last=0
    def __call__(self,row):
        if not self.tty:
            print(sanitize(json.dumps(row)),file=sys.stderr,flush=True);return
        now=time.monotonic()
        if now-self.last<.1 and row.get('phase') not in {'failed','interrupted','node_verified'}:return
        self.last=now;phase=row.get('phase','child_output');name=row.get('node',row.get('scene',''))
        counts=f" {row['completed']}/{row['total']}" if 'completed' in row and 'total' in row else ''
        width=__import__('shutil').get_terminal_size((80,24)).columns
        text=sanitize(f'{phase} {name}{counts} · {int(now-self.start)}s')[:max(15,width-2)]
        print('\r\x1b[2K'+text,file=sys.stderr,end='\n' if phase in {'failed','interrupted','node_verified'} else '',flush=True)
