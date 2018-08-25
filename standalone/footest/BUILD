python_library(
    name='lib',
    sources=rglobs('*.py'),
    compatibility='CPython>=3',
)

python_tests(name='tests',
  sources=rglobs('**/test_*.py'),
  dependencies=[
    ':lib',
  ],
  compatibility='CPython>=3',
)
