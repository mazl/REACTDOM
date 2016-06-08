class a {
	constructor(x, y) {
		this.x = x;
		this.y = y;
	}
	add() {
		return this.x + this.y;
	}
}

var fmp = new a(1, 2);

console.log(fmp.add());