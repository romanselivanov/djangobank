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
            <Field id="username" name="username" placeholder="email или телефон" />
            <Field type="password" id="password" name="password" placeholder="пароль" />
            <button type="submit">Login</button>
            <div style={{paddingTop: '50px'}}>
               {/* <Link href="/password-reset/">
                   <a>Забыли пароль?</a>
                </Link> */}
            </div>
        </Form>
    </Formik>
);

export default function LoginForm() {
    return (
        <div>
          <h2>Login</h2>
          {ContactForm}
          <div style={{paddingTop: '50px'}}>
            <button onClick={handleClick}>logout</button>
          </div>
        </div>
      );
}
