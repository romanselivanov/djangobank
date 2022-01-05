import { useRouter } from "next/router";
import Link from "next/link";
import styles from "../styles/Navbar.module.scss";
import Image from "next/image";

const navigation = [
    { id: 1, title: "Home", path: '/'},
    { id: 2, title: "Login", path: '/login'},
    { id: 3, title: "Accounts", path: '/accounts'},
];

const Navbar = () => {
    const { pathname } = useRouter();

    return (
    <nav className={styles.nav}>
        <div>
            <Image src='/logo.png' width={100} height={70} alt="logo" />
        </div>
        <div className={styles.links}>
            {navigation.map(({ id, title, path }) => (
                <Link key={id} href={path}>
                    <a className={ pathname === path ? styles.active : null }>{title}</a>
                </Link>
            ))}
        </div>
    </nav>
    );
};

export default Navbar;