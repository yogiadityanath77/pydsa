# Linked List & Doubly Linked List — Method Reference

A walkthrough of every method in `LL.py` (singly linked list) and `DLL.py`
(doubly linked list): what it does, the technique it uses, time/space cost,
and edge cases.

Notation: **n** = number of nodes. All lists track `head`, `tail`, `length`.

---

# Part 1 — `LL.py` (Singly Linked List)

Each `Node` holds `value` and a single `next` pointer. You can only move
forward, so anything that needs the *previous* node must carry a trailing
pointer or re-walk from the head.

## `Node.__init__(value)`
Stores `value`, sets `next = None`. The atomic unit of the list.

## `LinkedList.__init__(value)`
Creates one node and points both `head` and `tail` at it; `length = 1`.
**Note:** the list cannot be created empty — it always starts with one node.
Methods that check `self.length == 0` only matter *after* nodes are removed.

## `print_list()`
**Technique:** linear traversal with a single pointer.
Start `temp = head`, print `temp.value`, advance `temp = temp.next` until
`None`. O(n) time, O(1) space.

## `append(value)`
**Technique:** tail-pointer insertion.
Because `tail` is tracked, adding to the end is O(1): link `tail.next` to the
new node, then move `tail` forward. Handles the empty-list case by pointing
both `head` and `tail` at the new node. Returns `True`.

## `pop()`  — remove the last node
**Technique:** two-pointer trailing walk (`pre` follows `temp`).
A singly linked list has no back-pointer, so to drop the tail you must find
the *second-to-last* node. Walk `temp` to the end while `pre` stays one step
behind; then set `tail = pre`, `tail.next = None`. Decrement `length`; if it
hits 0, null out `head`/`tail`. O(n) time.
Returns the removed node (or `None` if empty).

## `prepend(value)`
**Technique:** head-pointer insertion.
New node's `next` points at the old `head`, then `head` moves to the new node.
O(1). Empty-list case points both ends at the new node. Returns `True`.

## `pop_first()`  — remove the first node
**Technique:** head advance.
Save `temp = head`, move `head = head.next`, detach `temp.next = None`.
O(1). Decrement `length`; if it reaches 0, also null `tail`.
Returns the removed node (or `None` if empty).

## `get(index)`
**Technique:** index-counted traversal.
Bounds-check `0 <= index < length`, then step forward `index` times from
`head`. O(n). Returns the **node** (not the value), or `None` if out of range.
This is the workhorse other methods reuse.

## `set_value(index, value)`
**Technique:** reuse `get()`.
Fetch the node; if it exists, overwrite `.value` and return `True`, else
`False`.

## `insert(index, value)`
**Technique:** split into cases + reuse `get(index - 1)`.
- `index == 0` → delegate to `prepend`
- `index == length` → delegate to `append`
- otherwise: get the node *before* the target, splice the new node in
  (`new.next = prev.next; prev.next = new`).
O(n) because of the walk. Rejects `index < 0` or `index > length`.

## `remove(index)`
**Technique:** case split + reuse `get(index - 1)` for the predecessor.
- `index == 0` → `pop_first`
- `index == length - 1` → `pop`
- otherwise: get predecessor, bypass the target
  (`prev.next = temp.next`), detach it.
O(n). Rejects `index < 0` or `index >= length`. Returns the removed node.

## `find_max()`
**Technique:** running-maximum linear scan.
Seed `maximum` with the first node, walk the rest, update whenever
`temp.value > maximum`. O(n). Returns `None` on an empty list.
*(Minor: `maximum` is seeded with the node but compared against values —
works for the return value, but mixing node and value is a code smell.)*

## `find_min()`
Same as `find_max()` with the comparison flipped (`<`).

## `count_occurance(value)`
**Technique:** linear scan with a counter.
Increment `count` every time `temp.value == value`. O(n). Returns the count
(0 if not found).

## `insert_after(target, value)`
**Technique:** linear search for the target value, then O(1) splice.
Walk until `temp.value == target` (or `None`). If not found, return `False`.
Otherwise splice the new node after `temp`.
**Known bugs:** `self.tail == new_node` is a comparison, not an assignment, so
the tail is never updated when inserting after the last node; the guard
`if temp.next == self.tail` is also the wrong check.

## `delete_occurances(value)`
**Technique:** two-phase removal —
1. **Leading run:** while `head` itself matches, advance `head` and shrink.
   Handles the case where the deleted value sits at the front.
2. **Body:** trailing-pointer walk (`prev`, `temp`). When `temp` matches,
   unlink it (`prev.next = temp.next`) and continue; otherwise advance both.
Finally fix `tail = prev`. Handles the list becoming empty. O(n), single pass.

## `reverse()`
**Technique:** in-place iterative reversal with three pointers
(`before`, `temp`, `after`).
First swap `head`/`tail`. Then for each node: remember `after = temp.next`,
flip `temp.next = before`, shift `before = temp`, `temp = after`.
O(n) time, O(1) space.
**Known bug:** crashes on an empty list (`temp.next` when `temp is None`).

## `find_middle_node()`
**Technique:** slow/fast (tortoise-and-hare) pointers.
`fast` moves two steps per `slow`'s one. When `fast` falls off the end,
`slow` is at the middle. For even n, `slow` lands on the second of the two
middle nodes. O(n) time, O(1) space, single pass.

## `has_loop()`
**Technique:** Floyd's cycle detection (slow/fast).
Advance `slow` by 1 and `fast` by 2 each iteration. If they ever meet, there
is a cycle → `True`. If `fast` reaches `None`, no cycle → `False`.
O(n) time, O(1) space.

## `find_kth_from_end(k)`
**Technique:** two pointers with a fixed gap of `k`.
Move `fast` `k` steps ahead first (returning `None` if the list is shorter
than `k`). Then advance `slow` and `fast` together until `fast` runs off the
end — `slow` is now `k` nodes from the end. O(n), single pass, O(1) space.

## `find_kth_from_beginning(k)`
**Technique:** index-counted traversal from the head.
Walk `k - 1` steps and return that node.
**Known bug:** bounds should be `k < 1 or k > self.length`; `k = 0` makes
`range(-1)` empty and returns the head instead of rejecting.

## `is_palindrome()`
**Technique:** find middle (slow/fast) + in-place reverse of the second half
+ inward two-pointer compare.
1. Trivial `True` for length ≤ 1.
2. Slow/fast to reach the midpoint.
3. Reverse the second half starting at `slow` (three-pointer flip).
4. Walk `left` from `head` and `right` from the reversed half's head,
   comparing values; any mismatch → not a palindrome.
5. Reverse the second half again to **restore** the original list.
O(n) time, **O(1) space** (no copy to an array).

---

# Part 2 — `DLL.py` (Doubly Linked List)

Each `Node` holds `value`, `next`, **and** `prev`. The back-pointer removes
the need for trailing-pointer walks: you can delete the tail in O(1) and
walk toward the middle from either end.

## `Node.__init__(value)`
Stores `value`; `next = None`, `prev = None`.

## `DoublyLinkedList.__init__(value)`
One node, `head = tail = node`, `length = 1`. Like the singly list, it cannot
start empty.

## `print_list()`
**Technique:** forward linear traversal from `head` via `next`. O(n).
*(No backward traversal method exists yet — it would start at `tail` and
follow `prev`.)*

## `append(value)`
**Technique:** tail insertion with back-linking.
Link `tail.next = new`, `new.prev = tail`, then move `tail`. O(1).
Empty-list case sets both ends. Returns `True`.

## `pop()`  — remove the last node
**Technique:** O(1) tail removal using `prev` (no walk needed — this is the
key DLL win over the singly list).
- length 1 → null both ends
- else → `tail = tail.prev`, `tail.next = None`, detach old node's `prev`.
Decrement `length`. Returns the removed node (or `None`).

## `prepend(value)`
**Technique:** head insertion with back-linking.
`new.next = head`, `head.prev = new`, move `head`. O(1).
**Note:** unlike `append`, this does **not** `return True` — so `insert(0, …)`
returns `None`.

## `pop_first()`  — remove the first node
**Technique:** O(1) head advance.
- length 1 → null both ends
- else → `head = head.next`, `head.prev = None`, detach old head's `next`.
Decrement `length`. Returns the removed node (or `None`).

## `get(index)`
**Technique:** bidirectional traversal — walk from whichever end is closer.
Bounds-check, then:
- if `index < length / 2` → step forward from `head`
- else → step backward from `tail` using `prev`
Still O(n) worst case but ~half the steps on average. Returns the node.
This optimization is only possible *because* of the `prev` pointer.

## `set_value(index, value)`
**Technique:** reuse `get()`; overwrite `.value` if the node exists.
Returns `True`/`False`.

## `insert(index, value)`
**Technique:** case split + reuse `get(index - 1)`, then a four-pointer splice.
- `index == 0` → `prepend`
- `index == length` → `append`
- otherwise: with `before` and `after = before.next`, set all four links:
  `new.prev = before`, `new.next = after`, `before.next = new`,
  `after.prev = new`.
O(n) for the walk. Rejects `index < 0` or `index > length`. Returns `True`.

## `remove(index)`
**Technique:** case split + `get(index)`, then unlink both directions.
- `index == 0` → `pop_first`
- `index == length - 1` → `pop`
- otherwise: `temp.next.prev = temp.prev`, `temp.prev.next = temp.next`,
  then detach `temp`'s own pointers.
No trailing pointer needed — `temp.prev` is right there. O(n) for the walk,
O(1) for the unlink. Returns the removed node.

---

# Technique Cheat-Sheet

| Technique | Where it's used |
|---|---|
| Single-pointer traversal | `print_list`, `find_max/min`, `count_occurance` |
| Index-counted walk | `get`, `find_kth_from_beginning` |
| Trailing / lagging pointer | `pop` (singly), `delete_occurances` |
| Head/tail pointer O(1) insert | `append`, `prepend` |
| Case split + delegate | `insert`, `remove` |
| Three-pointer in-place reversal | `reverse`, `is_palindrome` (step 3) |
| Slow / fast (tortoise & hare) | `find_middle_node`, `has_loop`, `is_palindrome` |
| Two pointers with a fixed gap | `find_kth_from_end` |
| Two-phase (leading run + body) | `delete_occurances` |
| Bidirectional (walk from nearer end) | DLL `get` |
| O(1) tail delete via `prev` | DLL `pop` |
| Four-pointer splice | DLL `insert`, DLL `remove` |

# Outstanding bugs (see checklist)
- `LL.reverse()` — crashes on empty list
- `LL.insert_after()` — tail not reassigned (`==` instead of `=`), wrong guard
- `LL.find_kth_from_beginning()` — bounds should be `k < 1 or k > length`
- `DLL.prepend()` — missing `return True`
