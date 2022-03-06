import React from 'react';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';

import Header from './components/Header';
import LogIn from './components/LogIn';
import SignUp from './components/SignUp';

function App() {

	return (
		<Router>
			<Header />
			<Switch>
				<Route path='/log-in'>
					<LogIn />
				</Route>
				<Route path='/sign-up'>
					<SignUp />
				</Route>
			</Switch>
		</Router>
	);
}

export default App;
