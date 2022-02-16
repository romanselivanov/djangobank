import * as apiAuth from '../api/auth'
import Link from "next/link";
import { Formik, Field, Form } from 'formik';

const handleClick = (e) =>  {
    apiAuth.logout().then(({data}) => {
        alert('success logout');
    }).catch((error) => {
        console.log(error)
    });
  }

const ContactForm = (
    <Formik
        initialValues={{
            username: '',
            password: '',
        }}

        onSubmit={(values) => {
            apiAuth.login(values.username, values.password).then(({data}) => {
                alert('success login')
            }).catch((error) => {
                console.log(error)
            });
        }}
    >
        <Form>
            <p><Field id="username" name="username" placeholder="email или телефон" /></p>
            <p><Field type="password" id="password" name="password" placeholder="пароль" /></p>
            <button type="submit">Login</button>
        </Form>
    </Formik>
);

export default function LoginForm() {
    return (
        <div style={{textAlign: 'center'}}>
          <h2>Login</h2>
          {ContactForm}
          <div style={{paddingTop: '20px'}}>
            <button onClick={handleClick}>Logout</button>
          </div>
          <div style={{paddingTop: '15px'}}>
            <Link href="/password-reset/">
                <a>Забыли пароль?</a>
            </Link>
          </div>
        </div>
      );
}
