while True:
    try:
        age = int(input("what is your age? "))
        10/age
        raise ValueError('hey cut it out')
    # except ValueError:
    #     print('please enter a number')
    #     continue
    except ZeroDivisionError:
        print('please enter age higher than 0')
        break
    else:
        print('thankyou')
        # break
    finally:
        print('ok, i am finally done')
    print('can you hear me?')