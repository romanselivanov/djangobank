import styles from "../styles/404.module.scss"
import { useEffect } from "react";
import { useRouter } from "next/router";

const NotFound = () => {
  const router = useRouter();

  useEffect(() => {
    setTimeout(() => {
      router.push('/');
    }, 3000);
  }, [router])

  return (
    <div className={styles.wrapper}>
      <h1>Page not found</h1>
    </div>
  )
};


export default NotFound;