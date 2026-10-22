"""Synthetic session-model checks; no network, secrets or target-system claims."""
import json
from pathlib import Path
class SessionModel:
    def __init__(self):self.sessions={};self.events=[]
    def event(self,action,label,result):self.events.append(dict(sequence=len(self.events)+1,action=action,synthetic_label=label,result=result))
    def login(self,old,rotate):
        new='synthetic-fresh-label' if rotate else old
        self.sessions.pop(old,None);self.sessions[new]='student-A';self.event('login',new,'issued');return new
    def request(self,label,owner='student-A'):
        result='allowed' if self.sessions.get(label)==owner else 'denied'
        self.event('request',label,result);return result
    def logout(self,label):self.sessions.pop(label,None);self.event('logout',label,'revoked')

def run():
    flawed=SessionModel();flawed.login('synthetic-known-label',False)
    assert flawed.request('synthetic-known-label')=='allowed'
    fixed=SessionModel();new=fixed.login('synthetic-known-label',True)
    assert fixed.request('synthetic-known-label')=='denied'
    assert fixed.request(new)=='allowed'
    assert fixed.request(new,'student-B')=='denied'
    fixed.logout(new);assert fixed.request(new)=='denied'
    # A toy half-open interval illustrates position checking, not full RFC TCP logic.
    assert 1000<=1100<2000 and not 1000<=3000<2000
    result=dict(status='passed',scope='offline synthetic model only; not production application acceptance',network_operations=0,real_credentials=0,checks=['flawed known identifier retained','old identifier denied after rotation','fresh identifier works','other owner denied','revoked identifier denied','toy interval distinction'],flawed_events=flawed.events,corrected_events=fixed.events)
    return result
if __name__=='__main__':
    import argparse
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path);args=p.parse_args();result=run();text=json.dumps(result,indent=2)+'\n'
    if args.output:args.output.write_text(text)
    print(text)
