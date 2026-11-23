from pathlib import Path
from protocol import main
from experiments import IDS,execute
if __name__=='__main__':raise SystemExit(main(Path(__file__).resolve().parent,IDS,execute))
