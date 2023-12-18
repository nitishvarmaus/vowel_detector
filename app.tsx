import React, { useState, useEffect } from 'react';

interface User {
  id: number;
  name: string;
  email: string;
}

const App: React.FC = () => {
  const [users, setUsers] = useState<User[]>([]);

  useEffect(() => {
    // Simulating fetching users from an API
    fetchUsers();
  }, []);

  const fetchUsers = async () => {
    try {
      const response = await fetch('https://jsonplaceholder.typicode.com/users');
      const data: User[] = await response.json();
      setUsers(data);
    } catch (error) {
      console.error('Error fetching users:', error);
    }
  };

  const renderUsers = () => {
    if (users.length === 0) {
      return <p>No users available.</p>;
    }

    return (
      <ul>
        {users.map((user) => (
          <li key={user.id}>
            {user.name} - {user.email}
          </li>
        ))}
      </ul>
    );
  };

  const greetUser = (user: User) => {
    alert(`Hello, ${user.name}!`);
  };

  const capitalizeString = (str: string): string => {
    return str.charAt(0).toUpperCase() + str.slice(1);
  };

  return (
    <div>
      <h1>TSX App with Functions</h1>
      {renderUsers()}
      <button onClick={() => greetUser(users[0])}>Greet First User</button>
      <p>Capitalized String: {capitalizeString('typescript')}</p>
    </div>
  );
};

export default App;
