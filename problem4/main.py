def count_item_and_sort(items):
    result = ""
    # create set of items, kemudian di-sort
    sort_items=sorted(sorted(set(items)),key=items.count)

    for i in sort_items:
        # cek index i di list sort_items
            if sort_items.index(i) < len(sort_items)-1:
                result +=f'{i}->{str(items.count(i))} '
            else: result +=f'{i}->{str(items.count(i))}'
    return result

if __name__ == "__main__":
    print(count_item_and_sort(["js", "js", "golang", "ruby", "ruby", "js", "js"]))
    # "golang->1 ruby->2 js->4"
    print(count_item_and_sort(["A", "B", "B", "C", "A", "A", "B", "A", "D", "D"]))
    # "C->1 D->2 B->3 A->4"
    print(count_item_and_sort(["football", "basketball", "tenis"]))
    # "basketball->1 football->1 tenis->1"