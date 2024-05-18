const cloneCarSymbol = Symbol('cloneCar');

export default class Car {
  constructor(brand, motor, color) {
    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }

  get brand() {
    return this._brand;
  }

  get motor() {
    return this._motor;
  }

  get color() {
    return this._color;
  }

  [cloneCarSymbol]() {
    const { _brand, _motor, _color } = this;
    return new this.constructor(_brand, _motor, _color);
  }

  cloneCar() {
    return this[cloneCarSymbol]();
  }
}
