pytest -s -v -n=3 -m "sanity" --html=./Reports\report.html testCases/ --browser chrome
rem pytest -s -v -n=3 -m "sanity and regression" --html=./Reports\report.html testCases/ --browser chrome
rem pytest -s -v -n=3 -m "sanity or regression" --html=./Reports\report.html testCases/ --browser chrome
rem pytest -s -v -n=3 -m "regression"--html=./Reports\report.html testCases/ --browser chrome


rem "rem" is used to comment in bat files