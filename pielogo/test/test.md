# Task

## Statement
### draw a "L" shape
		200 steps for one side and 150 steps for the other
<img src="4.gif" alt="" title="" width="450" />
```
FD(200)
LT(90)
FD(150)
```

## Simple loop
### draw a cirle loop
	    Circle: 50 steps in length for each edge
	    Turn 90 degrees right -> 4 circles
<img src="circle_loop.gif" alt="" title="" width="450" />
```
REPEAT (4, 
Circle(50),
RT(90)
)

```

## Learning into the loop and function
### Function_Loop1
		Suqare: 150 steps in length for each edge
		Turn 0 degrees right -> 4 squares
<img src="function_loop_1.gif" alt="" title="" width="450" />
```
REPEAT (4,
	REPEAT (4,
	FD(150),
	RT(90)
	)
)
```

### Function_Loop2
		Suqare: 150 steps in length for each edge
		Turn 30 degrees right -> 6 squares
<img src="function_loop_2.gif" alt="" title="" width="450" />
```
REPEAT (6,
	REPEAT (4,
	FD(150),
	RT(30)
	)
)
```


<!-- ### Function_Loop3
		Suqare: 150 steps in length for each edge
		Turn 45 degrees right -> 8 squares
<img src="function_loop_3.gif" alt="" title="" width="450" />


### Function_Loop4
		Suqare: 150 steps in length for each edge
		Turn 60 degrees right -> 12 squares
<img src="function_loop_4.gif" alt="" title="" width="450" /> -->