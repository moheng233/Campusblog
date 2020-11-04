

declare module "svelte-spa-router/wrap" {
    import { SvelteTypedComponent } from 'svelte-typed-component';
    import type { SvelteComponentDev } from 'svelte/internal';
    

    export interface WrappedComponent {
        component: SvelteComponent;
        conditions?: RoutePrecondition[] | RoutePreconditionAsync[];
        props?: {};
        userData?: {};
    }


    export function wrap<UC extends {}>(args: {
        component?: any,
        asyncComponent?: () => Promise<any>,
        loadingComponent?: SvelteTypedComponent,
        loadingParams?: SvelteTypedComponent,
        userData?: UC,
        props?: any,
        conditions?: (RoutePrecondition[] | RoutePrecondition) | (RoutePreconditionAsync[] | RoutePreconditionAsync)
    }): WrappedComponent;

    export default wrap;
}