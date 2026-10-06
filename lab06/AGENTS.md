# Lab 06 project rules

- REQUIREMENTS.md is the authoritative source of the acceptance criteria.
- Keep REQUIREMENTS.md and fees.py unchanged. This lab evaluates the supplied code.
- Use only the Python standard library.
- Write tests with unittest in tests/ and import the function using
  `from fees import late_fee`.
- Run tests from lab06 using `python3 -m unittest discover -s tests`.
- Test only whole-number inputs greater than or equal to zero, as specified.
- Derive expected fees from REQUIREMENTS.md, not from the implementation.
- Respect the active permission profile. Never request a command outside the
  sandbox, change permissions, or access the network.
- The tester reads REQUIREMENTS.md, writes tests/test_fees.py, and stops without
  running tests or inspecting fees.py.
- The reviewer reads REQUIREMENTS.md and fees.py, does not inspect tests/, changes
  no files, and stops after reporting violations in its reply.
- Record only observed results as evidence. Never claim an unperformed check passed.
