/*4-pricing.js*/

import Currency from './3-currency.js';


class Pricing {
    constructor (amount, currency) {
        if (typeof amount === 'number'
        && currency instanceof Currency) {
            this._amount = amount;
            this._currency = currency;
        }
        else {
            throw TypeError('Invalid attribute type');
        }
    }

    get amount() {
        return this._amount;
    }

    set amount(newAmount) {
        if (typeof newAmount === 'number') {
            this._amount = newAmount;
        }
        else {
            throw TypeError('Amount must be a number');
        }
    }

    get currency() {
        return this._currency;
    }

    set currency(newCurrency) {
        if (newCurrency instanceof Currency) {
            this._currency = newCurrency;
        }
        else {
            throw TypeError('Currency must be a Currency');
        }
    }

    displayFullPrice() {
        return `${this.amount} ${this.currency.displayFullCurrency()}`;
    }

    static convertPrice(amount, conversionRate) {
        if (typeof amount === 'number'
        && typeof conversionRate === 'number') {
            return new Pricing(amount * conversionRate, this.currency);
        }
        else {
            throw TypeError('Invalid attribute type');
        }
    }
}

export default Pricing;
