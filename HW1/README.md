# HW1 · Group Trip Budget Calculator

## Run from the Homeworks repository root
python3 HW1/main.py

## Example run
Inputs:
Travelers: 4
Nights: 2
Nightly accommodation cost: 120
Total transportation cost: 80
Daily food cost per person: 15

Outputs:
Total accommodation cost: 240
Total food cost: 180
Total trip cost: 500
Cost per traveler: 125.0

## Prediction before the second run
If the number of travelers doubles from 4 to 8 while all other inputs stay fixed, I expect the following:
-Total accommodation cost will stay the same at 240, because accommodation is calculated for the whole group.
-Total food cost doubles from 180 to 360, as it depends on the number of travelers.
-Total trip cost will increase from 500 to 680 due to the higher food expenses.
-As a result cost per traveler decreases from 125.0 to 85.0 because the total trip cost is shared among more travelers.

## Observed second run and explanation
Record the new entries/results and compare them with your prediction. Explain what you checked; correcting your prediction is welcome.

The second run.

Inputs:
melani@MacBook-Pro-Melani Homeworks % python3 HW1/main.py
Travelers: 8
Nights: 2
Nightly accommodation cost: 120
Total transportation cost: 80
Daily food cost per person: 15

Outputs:
Total accommodation cost: 240
Total food cost: 360
Total trip cost: 680
Cost per traveler: 85.0
melani@MacBook-Pro-Melani Homeworks % 

Comparison and explanation:
The actual results matched my initial prediction. The accommodation cost remained unchanged because it applies to the entire group, while the food cost doubled because it depends on the number of travelers. As a result, the total trip cost increased from 500 to 680, and the cost per traveler decreased from 125.0 to 85.0.
I checked the calculations by comparing the results of both runs and confirming that only the number of travelers had changed. This demonstrated how the number of travelers affects the group expenses and the individual cost.

## AI assistance
AI assistance was used only for GitHub repository setup and troubleshooting folder-location issues in the terminal. 

## Work time or support (optional)
Approximately 1 hour.
