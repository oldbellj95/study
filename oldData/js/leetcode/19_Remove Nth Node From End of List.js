/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} n
 * @return {ListNode}
 */
var removeNthFromEnd = function(head, n) {
    var next = NaN;
    var heads = [];
    while(next != null){
        heads.push(head.val);
        next = head.next;
        if(next != null){
            head = next;
        }
    }
    heads.pop()
    console.log(heads);
};

아직 다 못함.