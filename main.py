import basics.output.simple_message as simple_message

import basics.output.multiline_message as multiline_message

import basics.output.escape_characters as escape_characters

import basics.output.ascii_art as ascii_art

import basics.input.user_input as user_input

import basics.input.string_operators as string_operators

import basics.input.review1 as review1

import basics.input.data_types as data_types

import basics.input.ascii_robot as ascii_robot

import basics.decisions.and_operator as and_operator

import basics.decisions.or_operator as or_operator

import basics.decisions.review2 as review2 

import basics.decisions.nested_decision.nestception as nestception

import basics.decisions.nested_decision.nested as nested

import basics.decisions.simple_decisions.comparison_operators as comparison_operators

import basics.decisions.simple_decisions.counter as counter 

import basics.decisions.simple_decisions.if_elif_else as if_elif_else

import basics.decisions.simple_decisions.if_else as if_else

import basics.decisions.simple_decisions._if as _if

import basics.decisions.simple_decisions.modulus_operator as modulus_operator

import basics.repetitions.for_loop.simple as simple

import basics.repetitions.for_loop.reverse as reverse

import basics.repetitions.for_loop._range as _range

import basics.repetitions.for_loop.membership_operators as membership_operators

import basics.repetitions.for_loop.count_down as count_down

import basics.repetitions.for_loop.characters as characters

import basics.repetitions.nested_loop.nested as nested

import basics.repetitions.nested_loop.nesting as nesting

import basics.repetitions.while_loop.sum_user_numbers as sum_user_numbers

import basics.repetitions.while_loop.sum_100 as sum_100

import basics.repetitions.while_loop.simple as simple

import basics.repetitions.while_loop.len as len

import basics.repetitions.while_loop.factorial as factorial

import basics.repetitions.while_loop.count as count

import basics.repetitions.while_loop.ascii as ascii



def run_block_a():
    print("Which program in 'Block A: Basics' do you wish to run?")
    response = input()
    if (response == "simple_message"):
        simple_message.run()
    elif (response == "multiline_message"):
        multiline_message.run()
    elif (response == "escape_characters"):
        escape_characters.run()
    elif (response == "ascii_art"):
        ascii_art.run()
    elif (response == "user_input"):
        user_input.run()
    elif (response == "string_operators"):
        string_operators.run()
    elif (response == "review2"):
        review2.run()
    elif (response == "data_types"):
        data_types.run()
    elif (response == "ascii_robot"):
        ascii_robot.run()
    elif (response == "and_operator"):
        and_operator.run()
    elif (response == "or_operator"):
        or_operator.run()
    elif (response == "review1"):
        review1.run()
    elif (response == "nestception"):
        nestception.run()
    elif (response == "nested"):
        nested.run()
    elif (response == "comparison_operators"):
        comparison_operators.run()
    elif (response == "counter"):
        counter.run()
    elif (response == "if_elif_else"):
        if_elif_else.run()
    elif (response == "if_else"):
        if_else.run()
    elif (response == "_if"):
        _if.run()
    elif (response == "modulus_operator"):
        modulus_operator.run()
    elif (response == "simple"):
        simple.run()
    elif (response == "reverse"):
        reverse.run()
    elif (response == "_range"):
        _range.run()
    elif (response == "membership_operators"):
        membership_operators.run()
    elif (response == "count_down"):
        count_down.run()
    elif (response == "characters"):
        characters.run()
    elif (response == "nested"):
        nested.run()
    elif (response == "nesting"):
        nesting.run()
    elif (response == "sum_user_numbers"):
        sum_user_numbers.run()
    elif (response == "sum_100"):
        sum_100.run()
    elif (response == "simple"):
        simple.run()
    elif (response == "len"):
        len.run()
    elif (response == "factorial"):
        factorial.run()
    elif (response == "count"):
        count.run()
    elif (response == "ascii"):
        ascii.run()


def run():
    is_running = True

    while(is_running):
        print("What would you like to do?")
        print("[a] Run 'Block A: Basics' programs")
        print("[q] Quit")
        response = input()

        if (response == "a"):
            run_block_a()
        elif (response == "q"):
            break
        else:
            print("Invalid option! Please try again.")

run()


def run():
    is_running = True

    while(is_running):
        print("What would you like to do?")
        print("[a] Run 'Block A: Basics' programs")
        print("[q] Quit")
        response = input()

        if (response == "a"):
            run_block_a()
        elif (response == "q"):
            break
        else:
            print("Invalid option! Please try again.")

run()