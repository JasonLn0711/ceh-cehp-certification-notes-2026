import unittest, subprocess, sys, os
from pathlib import Path


class CLISignalContract(unittest.TestCase):
    def test_sigterm_closes_attempt(self):
        script = "import json,os,signal,subprocess,sys,tempfile\nfrom pathlib import Path\nwith tempfile.TemporaryDirectory() as tmp:\n code='''import sys,time\nfrom pathlib import Path\nfrom types import SimpleNamespace\nfrom ceh_video import __main__ as cli,runner\np=SimpleNamespace(root=Path(sys.argv[1]),qa=Path(sys.argv[1]))\ncli.Project=lambda _:p\ndef work(p,target,forced,emit):\n emit({'phase':'node_start','node':'signal-test'})\n print('READY',flush=True)\n time.sleep(60)\nrunner._run=work\nsys.argv=['ceh-video','--project',str(p.root),'--plain','run','--target','signal-test','--run-kind','migration']\nraise SystemExit(cli.main())\n'''\n child=subprocess.Popen([sys.executable,'-c',code,tmp],stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)\n assert child.stdout.readline().strip()=='READY'\n child.send_signal(signal.SIGTERM)\n stdout,stderr=child.communicate(timeout=10)\n summaries=list(Path(tmp).glob('runs/*/summary.json'));assert len(summaries)==1\n summary=json.loads(summaries[0].read_text())\n assert child.returncode==130 and summary['status']=='interrupted' and summary['error']=='Received SIGTERM'\n print(json.dumps({'status':'passed','actual_signal':'SIGTERM','exit_code':child.returncode,'summary_status':summary['status'],'scope':'CLI termination reaches runner immutable-attempt closeout; no render or model execution'}))\n"
        result = subprocess.run([sys.executable, "-c", script], capture_output=True, text=True, timeout=15)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn('"status": "passed"', result.stdout)
