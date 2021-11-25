from sample_madlibs import propaganda, kotek, pogoda
import random 

if __name__ == "__main__":
  m = random.choice([propaganda, kotek, pogoda ])
  m.madlib()
