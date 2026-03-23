```
Py102_batch01/                      ← root
├── submissions/                    ← parent node
│   ├── PY102001001/                ← student folder (internal node)
│   │   ├── lab00.py                ← leaf (file)
│   │   └── lab01.py
│   │   
│   ├── Y102001002/
│   │   ├── lab00.py
│   │   └── lab02.py
│   └── ...
├── autograder/                     ← another subtree
│   ├── tests/                      ← internal node
│   │   ├── test_lab00.py           ← leaf
│   │   └── test_lab01.py
│   ├── run_grader.py               ← leaf
│   └── config.json                 ← leaf
├── .github/                         ← subtree 
│   ├── lab00.py
│   └── lab01.py
└── README.md                       ← leaf
```

```
        50
       /  \
     30    70
    /  \   /  \
   20  40 60   80
```

```
                         Py102_batch01
           ┌───────────────────────┼───────────────────┬───────────────┐
      submissions                autograder          .github     README.md
           │                       │                   │
     ┌─────┴─────┐            ┌────┴────┐         ┌────┴────┐
  PY102001001    PY102001001  tests   grade.py   scripts   workflows
     │             │                   
  ┌──┼──┐       ┌──┴──┐  
lab00 lab01 lab00  lab01  
```