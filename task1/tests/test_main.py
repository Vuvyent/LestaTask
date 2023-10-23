import pytest

from ..src.main import main


@pytest.fixture(scope="module")
def get_table():
    sites_table = main()
    print("data collected")
    return sites_table


@pytest.fixture()
def get_error_idx(get_table, request):
    num = request.param
    list_of_error_idx = []
    for i in range(len(get_table.list_of_websites)):
        if get_table.list_of_websites[i].popularity < num:
            list_of_error_idx.append(i)
    yield list_of_error_idx
    if len(list_of_error_idx) != 0:
        request.node.add_marker(pytest.mark.xfail(reason="..."))
        pr = request.param
        mstr = ""
        for i in range(len(list_of_error_idx)):
            frontend_str = ""
            backend_str = ""
            for j in range(len(get_table.list_of_websites[i].frontend)):
                frontend_str += get_table.list_of_websites[i].frontend[j] + ","
            for j in range(len(get_table.list_of_websites[i].backend)):
                backend_str += get_table.list_of_websites[i].backend[j] + ","
            mstr = get_table.list_of_websites[i].name + "(Frontend:" + frontend_str + "|Backend:" + backend_str + \
                   ") has " + str(get_table.list_of_websites[i].popularity) + \
                   " unique visitors per month. (Expected more than " + str(pr) + ")"
            print(mstr)


@pytest.mark.parametrize("get_error_idx", [10**7, 1.5*(10**7), 5*(10**7), 10**8, 5*(10**8), 10**9, 1.5*(10**9)],
                         indirect=True)
def test_main(get_error_idx, get_table):
    assert len(get_error_idx) == 0

