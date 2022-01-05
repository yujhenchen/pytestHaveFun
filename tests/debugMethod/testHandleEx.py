import traceback


def test_handle_ex():
    try:
        print("do something")
        raise Exception("custom Exception")
    except Exception as ex:
        print("catch the exception: " + str(ex))
        traceback.print_exc()
    finally:
        print("finally do something")


test_handle_ex()