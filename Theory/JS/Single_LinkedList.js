class Node {
  // 생성자
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

class SinglyLinkedList {
  constructor() {
    // 헤드와 테일 포인터로 구성
    this.head = null;
    this.tail = null;
  }

  find(value) {
    let currNode = this.head;
    // 값을 찾을 때까지  다음 요소 돌림
    while (currNode.value !== value) {
      // 값 찾으면 해당 노드 반환
      currNode = currNode.next;
    }
    return currNode;
  }

  append(newValue) {
    // 요소 중간 추가
    const newNode = new Node(newValue);
    if (this.head === null) {
      this.head = newNode;
      this.tail = newNode;
    } else {
      this.tail.next = newNode;
      this.tail = newNode;
    }
  }

  insert(node, newValue) {
    // 요소 끝에 추가
    const newNode = new Node(newValue);
    newNode.next = node.next;
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
  }

  display() {
    let currNode = this.head;
    let displayString = "[";
    while (currNode !== null) {
      displayString += `${currNode.value}, `;
      currNode = currNode.next;
    }
    displayString = displayString.substr(0, displayString.length - 2);
    displayString += "]";
    console.log(displayString);
  }
}
