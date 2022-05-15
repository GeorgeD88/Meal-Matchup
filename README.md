# Meal Matchup
**Meal Matchup** is a simple program that makes ordering fast food easier. Whenever you order food with a bunch of friends, one person just wants large fries while another wants a sandwich and a drink but then another person wants small fries and it just keeps going on. When it comes to finally ordering, you have a bunch of individual foods in varying sizes that could probably be ordered a lot easier as meals. **Meal Matchup** aims to solve this by matching up as many individual items into meals, making it easier and cheaper to order.

## How to run
The program is contained in one little script so it's really simple to use. The only thing you might need to watch out for is how you input things, so here's a little guide.<br>

<u>The basic form is `TYPE SIZE ITEM`</u><br>
`TYPE` is the type of item you're entering: **D** for drink, **F** for fries, and **I** for item (like burger).<br>
`SIZE` is the size of what you're entering **(S/M/L)**, the catch is only fries and drinks come in different sizes so when you enter something of type **I**, you don't want to enter it with a size.<br>
`ITEM` is what you're actually ordering, so like the drink or sandwich name, this is where there's another catch. For fries, the name is almost always just "fries" so unless you're ordering some special type of fries (like chilli cheese fries) then just leave the item name blank and it will be filled in automatically as "fries".<br>

That's all there is to it. This was a pretty quick code that probably didn't even take an hour so there could be some broken edge cases, but it was just supposed to be a fun little program anyways.