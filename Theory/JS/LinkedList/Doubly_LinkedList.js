class Node {
  // 생성자
  constructor(value) {
    this.value = value;
    this.prev = null;
    this.next = null;
  }
}

class DoublyLinkedList {
  constructor() {
    this.head = null;
    this.tail = null;
  }

  find(value) {
    let currNode = this.head;
    // 값을 찾을 때까지  다음 요소 돌림
    while (currNode.value !== value) {
      // 값 찾으면 해당 노드 반환
      currNode = currNode.next;
      if (currNode === null) {
        // 값이 없을 경우 에러 처리
        return "해당 값을 찾을 수 없습니다.";
      }
    }

    return currNode;
  }

  append(newValue) {
    // 요소 끝에 추가
    const newNode = new Node(newValue);
    if (this.head === null) {
      this.head = newNode;
      this.tail = newNode;
    } else {
      this.tail.next = newNode;
      newNode.prev = this.tail;
      this.tail = newNode;
    }
  }

  insert(node, newValue) {
    // 요소 중간 추가
    if (node === "해당 값을 찾을 수 없습니다.") {
      console.log("중간에 넣을 값을 찾을 수 없습니다.");
      return;
    }

    const newNode = new Node(newValue);
    newNode.next = node.next;
    node.next.prev = newNode;
    newNode.prev = node;
    node.next = newNode;
  }

  remove(value) {
    let prevNode = this.head;
    while (prevNode.next.value !== value) {
      prevNode = prevNode.next;
    }

    if (prevNode.next !== null) {
      prevNode.next = prevNode.next.next;
    }
    prevNode.next.prev = prevNode;
    console.log(prevNode);
  }

  display() {
    let currNode = this.head;
    let displayString = "[";
    while (currNode !== null) {
      displayString += `${currNode.value}, `;
      currNode = currNode.next;
    }
    if (displayString !== "[") {
      // LinkedList가 비어있을 때 에러처리
      displayString = displayString.substring(0, displayString.length - 2);
    }

    displayString += "]";
    console.log(displayString);
  }

  size() {
    let currNode = this.head;
    let count = 0;
    while (currNode !== null) {
      count += 1;
      currNode = currNode.next;
    }
    return count;
  }
}

const linkedList = new DoublyLinkedList();
linkedList.append(1);
linkedList.append(2);
console.log(linkedList.find(3));
linkedList.insert(linkedList.find(1), 7);
linkedList.display();
linkedList.remove(7);
linkedList.display();
console.log(linkedList.size());
