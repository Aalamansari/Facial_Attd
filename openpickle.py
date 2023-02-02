import pickle
import os

data = pickle.loads(open('init_data'+os.path.sep+'encodings.pickle','rb',).read())
print(data)