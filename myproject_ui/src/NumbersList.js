import  React, { Component } from  'react';
import  NumbersService  from  './NumbersService';

const  numbersService  =  new  NumbersService();

class  NumbersList  extends  Component {

constructor(props) {
	super(props);
	this.state  = {
		numbers: [],
	};
}

componentDidMount() {
	var  self  =  this;
	numbersService.getNumbers().then(function (result) {
		self.setState({ numbers:  result})
	});
}
render() {

	return (
		<div  className="numbers--list">
			<table  className="table">
			<thead  key="thead">
			<tr>
			    <th>номер</th>
				<th>заказ</th>
				<th>цена $</th>
				<th>дата поставки</th>
				<th>цена руб</th>
			</tr>
			</thead>
			<tbody>
			{this.state.numbers.map( c  =>
				<tr  key={c.pk}>
				<td>{c.number}</td>
				<td>{c.order}</td>
				<td>{c.price_dollar}</td>
				<td>{c.delivery_data}</td>
				<td>{c.price_rub}</td>
			</tr>)}
			</tbody>
			</table>
		</div>
		);
  }
}
export  default  NumbersList;