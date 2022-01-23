import styles from "../styles/Index.module.scss";
import * as apiAccounts from '../api/accounts'
import { useState, useEffect } from 'react';


const Accounts = () => {
  const [accounts, setAccounts] = useState(null);

  useEffect(() => {
    apiAccounts.list(`accounts/`).then((response) => {
      setAccounts(response.data);
    }).catch((error) => {});
  }, [accounts]);

  return (
    <div className={styles.wrapper}>
      <h2>Аккаунты: </h2>
      {accounts && accounts.map(({description, rate, type}) => (
        <ul key={type}>баланс: {rate} описание: {description} тип: {type}</ul>
      ))}
    </div>
  );
}


export default Accounts;
