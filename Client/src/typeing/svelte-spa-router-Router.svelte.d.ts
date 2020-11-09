// import { SvelteTypedComponent } from 'svelte-typed-component';


// declare module "svelte-spa-router/Router" {
//     import type { derived, Readable } from 'svelte/store';
//     import type { WrappedComponent } from 'svelte-spa-router/wrap'



//     interface _RouterProps {
//         routes: {
//             [keys: string]: WrappedComponent
//         },
//         restoreScrollState: boolean
//     }

//     interface Location {
//         location: string,
//         querystring?: string
//     }

//     export default class Router extends SvelteTypedComponent<_RouterProps, {}> {
//         /**
//          * Returns the current location from the hash.
//          *
//          * @returns Location object
//          * @private
//          */
//         getLocation(): Location;


//         loc: Readable<Location>
//         /**
//          * Readable store that returns the current location
//          */
//         export const location: derived<loc, string>;
//         /**
//          * Readable store that returns the current querystring
//          */
//         export const querystring: derived<loc, string>;

//         /**
//          * Navigates to a new page programmatically.
//          *
//          * @param location - Path to navigate to (must start with `/` or '#/')
//          * @return Promise that resolves after the page navigation has completed
//          */
//         export async push(location: string): Promise<void>

//         /**
//          * Navigates back in history (equivalent to pressing the browser's back button).
//          *
//          * @return Promise that resolves after the page navigation has completed
//          */
//         export async pop(): Promise<void>

//         /**
//          * Replaces the current page but without modifying the history stack.
//          *
//          * @param location - Path to navigate to (must start with `/` or '#/')
//          * @return Promise that resolves after the page navigation has completed
//          */
//         export async replace(location: string): Promise<void>

//         /**
//          * Svelte Action that enables a link element (`<a>`) to use our history management.
//          *
//          * For example:
//          *
//          * ````html
//          * <a href="/books" use:link>View books</a>
//          * ````
//          *
//          * @param node - The target node (automatically set by Svelte). Must be an anchor tag (`<a>`) with a href attribute starting in `/`
//          * @param hrefVar - A string to use in place of the link's href attribute. Using this allows for updating link's targets reactively.
//          */
//         export link(node: HTMLElement, hrefVar: string)
//     }
// }

