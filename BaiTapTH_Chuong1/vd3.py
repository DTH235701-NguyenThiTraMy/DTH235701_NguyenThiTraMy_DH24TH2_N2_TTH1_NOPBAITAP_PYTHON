#module1.py
question = 'What is the meaning of Life, the Universe, and Everything?'
answer = 42

#module2.py
question = 'What is your quest?'
answer = 'To seek the holy grail.'

import module1
import module2
print(module1.question)
print(module2.question)
print(module1.answer)
print(module2.answer)